<template>
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
    <div class="main-left">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <h1 class="mb-6 text-2xl">Sign up</h1>
        <p class="mb-6 text-gray-500">
          Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum
          dolor sit mate. Lorem ipsum dolor sit mate. Lorem ipsum dolor sit
          mate. Lorem ipsum dolor sit mate.
        </p>

        <p class="font-bold">
          Already have an account?
          <RouterLink :to="{ name: 'login' }" class="underline"
            >Click here</RouterLink
          >
          to log in!
        </p>
      </div>
    </div>

    <div class="main-right space-y-4">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <form class="space-y-6" v-on:submit.prevent="submitForm">
          <div>
            <label>Name</label><br />
            <input
              v-model="form.name"
              type="text"
              placeholder="Your full name"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <div>
            <label>E-mail</label><br />
            <input
              v-model="form.email"
              type="email"
              placeholder="Your e-mail address"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <div>
            <label>Password</label><br />
            <input
              v-model="form.password1"
              type="password"
              placeholder="Your password"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <div>
            <label>Repeat Password</label><br />
            <input
              v-model="form.password2"
              type="password"
              placeholder="Repeat your password"
              class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg"
            />
          </div>

          <template v-if="errors.length > 0">
            <div class="bg-red-300 text-white rounded-lg p-6">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
          </template>

          <div>
            <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">
              Sign up
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { useToastStore } from "@/stores/toast";
import { useUserStore } from "@/stores/user";

export default {
  setup() {
    const toastStore = useToastStore();
    const userStore = useUserStore();

    return {
      toastStore,
      userStore,
    };
  },

  data() {
    return {
      form: {
        email: "",
        name: "",
        password1: "",
        password2: "",
      },
      errors: [],
    };
  },

  methods: {
    async submitForm() {
      this.errors = [];

      if (this.form.email === "") this.errors.push("Your e-mail is missing");
      if (this.form.name === "") this.errors.push("Your name is missing");
      if (this.form.password1 === "")
        this.errors.push("Your password is missing");
      if (this.form.password2 !== this.form.password2)
        this.errors.push("The password does not match");

      if (this.errors.length === 0) {
        await axios
          .post("/api/signup/", this.form)
          .then((response) => {
            if (response.data.message === "success") {
              this.toastStore.showToast(
                5000,
                "The user is registered. Please activate your account by clicking your email link.",
                "bg-emerald-500"
              );

              // Clear form data
              this.form.email = "";
              this.form.name = "";
              this.form.password1 = "";
              this.form.password2 = "";
            } else {
              const data = JSON.parse(response.data.message);
              for (const key in data) {
                this.errors.push(data[key][0].message);
              }

              this.toastStore.showToast(
                5000,
                "Something went wrong. Please try again",
                "bg-red-300"
              );
            }
          })
          .catch((error) => {
            console.log("error", error);
          });
      }
    },
  },

  beforeCreate() {
    const token = this.userStore.user.isAuthenticated;
    if (token) {
      this.$router.push("/feed");
    }
  },
};
</script>
