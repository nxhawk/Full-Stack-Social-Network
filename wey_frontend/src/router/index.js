import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SignupView from "../views/SignupView.vue";
import LoginView from "../views/LoginView.vue";
import FeedView from "../views/FeedView.vue";
import ProfileView from "../views/ProfileView.vue";
import SearchView from "../views/SearchView.vue";
import FriendsView from "../views/FriendsView.vue";
import PostView from "../views/PostView.vue";
import ChatView from "../views/ChatView.vue";
import TrendView from "../views/TrendView.vue";
import EditProfileView from "../views/EditProfileView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/signup",
      name: "signup",
      component: SignupView,
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/feed",
      name: "feed",
      component: FeedView,
    },
    {
      path: "/profile/:id",
      name: "profile",
      component: ProfileView,
    },
    {
      path: "/search",
      name: "search",
      component: SearchView,
    },
    {
      path: "/chat",
      name: "chat",
      component: ChatView,
    },
    {
      path: "/profile/:id/friends",
      name: "friends",
      component: FriendsView,
    },
    {
      path: "/:id",
      name: "postview",
      component: PostView,
    },
    {
      path: "/trends/:id",
      name: "trendview",
      component: TrendView,
    },
    {
      path: "/profile/edit",
      name: "editprofile",
      component: EditProfileView,
    },
    // {
    //   path: "/about",
    //   name: "about",
    //   component: () => import("../views/AboutView.vue"),
    // },
  ],
});

export default router;
