import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";

Vue.config.productionTip = false;

Vue.filter("dateFormater", (val) => {
  const months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];
  const datetime = new Date(val);
  let formatted_date = `${
    months[datetime.getMonth()]
  } ${datetime.getDate()}, ${datetime.getFullYear()}, ${datetime.getHours()}:${datetime.getMinutes()}`;
  return formatted_date;
});

new Vue({
  router,
  store,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
