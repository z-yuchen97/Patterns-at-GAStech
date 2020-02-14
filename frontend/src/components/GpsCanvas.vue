<template>
  <div>
    {{ gps_info }}
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "GpsCanvas",
  data() {
    return {
      gps_info: []
    };
  },
  mounted(){
    this.search()
  },
  methods: {
    search: async function() {
      const res = await axios.get('api/search_gps', {
        params: {
          firstname: this.$route.query.firstname,
          lastname: this.$route.query.lastname,
          time_start: this.$route.query.time_start,
          time_end: this.$route.query.time_end
          }
        }
      );
      this.gps_info = res.data;
      console.log(this.$route.query.time_start)
    }
  }
};
</script>




<style scoped>

</style>