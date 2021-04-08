<template>
  <div>
    <v-snackbar auto-height :color="currentNotificationColor" v-model="show">
      <v-progress-circular
        class="ma-2"
        indeterminate
        v-show="showProgress"
      ></v-progress-circular
      >{{ currentNotificationContent }}
      <v-btn flat @click.native="close">关闭</v-btn>
    </v-snackbar>
  </div>
</template>

<script>
export default {
  data() {
    return {
      show: false,
      text: "",
      showProgress: false,
      currentNotification: false
    };
  },
  methods: {
    async hide() {
      this.show = false;
      await new Promise((resolve, reject) => setTimeout(() => resolve(), 500));
    },
    async close() {
      await this.hide();
      await this.removeCurrentNotification();
    },
    async removeCurrentNotification() {
      if (this.currentNotification) {
        commitRemoveNotification(this.$store, this.currentNotification);
      }
    }
  }
};
</script>
