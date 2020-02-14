<template>
  <div>
    <h1>Kronos Incident</h1>
    <div id="search">
      <div id="name-search">
        <strong>Firstname:</strong>
        <select v-model="firstname" class="select" style="width:120px;">
            <option disabled value selected>--Firstname--</option>
            <option v-for="(pinfo, index) in personal_info" :key="index">{{pinfo.firstname}}</option>
        </select>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <strong>Lastname:</strong>
        <select v-model="lastname" class="select" style="width:120px;">
            <option disabled value selected>--Lastame--</option>
            <option v-for="(pinfo, index) in personal_info" :key="index">{{pinfo.lastname}}</option>
        </select>
      </div>
      <div id="time-search">
        <strong>From:</strong>
        <select v-model="start_date" class="time" style="width:70px;">
          <option disabled value selected>-date-</option>
          <option v-for="(d, index) in time_info.date" :key="index">{{d}}</option>
        </select>
        <select v-model="start_hour" class="time" style="width:70px;">
          <option disabled value selected>-hour-</option>
          <option v-for="(h, index) in time_info.hour" :key="index">{{h}}</option>
        </select>
        <select v-model="start_minute" class="time" style="width:90px;">
          <option disabled value selected>-minute-</option>
          <option v-for="(m, index) in time_info.minute" :key="index">{{m}}</option>
        </select>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <strong>To:</strong>
        <select v-model="end_date" class="time" style="width:70px;">
          <option disabled value selected>-date-</option>
          <option v-for="(d, index) in time_info.date" :key="index">{{d}}</option>
        </select>
        <select v-model="end_hour" class="time" style="width:70px;">
          <option disabled value selected>-hour-</option>
          <option v-for="(h, index) in time_info.hour" :key="index">{{h}}</option>
        </select>
        <select v-model="end_minute" class="time" style="width:90px;">
          <option disabled value selected>-minute-</option>
          <option v-for="(m, index) in time_info.minute" :key="index">{{m}}</option>
        </select>
        <br>
        <button @click="searchRange">Search</button>
      </div>
    </div>
    <div>
      <div id="point"></div>
      <div id="map"></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SearchGps",
  data() {
    return {
      personal_info: [],
      time_info: [],
      gps_info: "",
      dataset: [],
      firstname: "",
      lastname: "",
      start_date: "",
      start_hour: "",
      start_minute: "",
      end_date: "",
      end_hour: "",
      end_minute: ""
    };
  },

  mounted() {
    // generate page when first load
    axios.get("/api/init_person")
          .then(response => (this.personal_info = response.data));
    axios.get("/api/init_time")
          .then(response => (this.time_info = response.data));
  },

  methods: {
    searchRange: async function(){
      if(this.start_date == ""){
        alert("Please Input Date");
      }else{
        var time_start = "14-1-" + this.start_date + " " + this.start_hour + ":" + this.start_minute
        var time_end = "14-1-" + this.end_date + " " + this.end_hour + ":" + this.end_minute
        console.log(time_start);
        console.log(time_end);
        const res = await axios.get('api/search_gps', {
          params: {
            firstname: this.firstname,
            lastname: this.lastname,
            time_start: time_start,
            time_end: time_end
            }
          }
        );
        // this.gps_info = JSON.stringify(res.data);
        this.gps_info = res.data;

        this.render();
      }
    },

    render: function(){
      var delete_svg = document.getElementById("canvas")
      if(delete_svg != null){
        delete_svg.remove();
      }
      //Create SVG element
      let w = 600;
      let h = 300;
      let svg = d3.select("#point")
                  .append("svg")
                  .attr("width", w)
                  .attr("height", h)
                  .attr("id", "canvas");
      
      let tip = d3.tip()
        .attr('class', 'd3-tip')
        .offset([-10, 0])
        .html(function(d) {
                return "<span style='color:violet'>" + d.firstname + " " + d.lastname + 
                "</span><br>TimeStamp:<span style='color:pink'>" + d.timestamp
        })

      let x = d3.scaleLinear()
        .domain([24.82508806, 24.90848537])
        .range([0, w]);         
      let y = d3.scaleLinear()
        .domain([36.04802098, 36.08995956])
        .range([h, 0]);
      let dataset = [];
      dataset = this.gps_info;

      svg.call(tip)
      svg.selectAll("rect")
        .data(dataset)
        .enter()
        .append("rect")
        .attr("width", 2)
        .attr("height", 2)
        .attr("fill", function(d, index){
          return "black"
        })
        .attr("x", (d) => x(d.longtitude))
        .attr("y", (d) => y(d.latitude))
        .on('mouseover', function(d){
          d3.select(this)
          .attr("fill", "orange");
          tip.show(d);
        })
        .on('mouseout', function(d){
          d3.select(this)
          .attr("fill", "black");
          tip.hide(d);
        })
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  text-align: center;
}

h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}




#search {
  height: 100px;
  text-align: center;
}

#map {
  background-image: url(../../../backend/patterns/A2_Data/MC2-tourist.jpg);
  background-size: 600px 320px;
  background-repeat: no-repeat;
  opacity: 0.7;
  width: 600px;
  height: 350px;
  position: absolute;
  top: 230px;
  z-index: -1;
}

#point {
  width: 600px;
  height: 300px;
  position: absolute;
  top: 230px;
  z-index: 0;
}

.d3-tip {
    line-height: 1;
    font-weight: bold;
    padding: 12px;
    background: rgba(0, 0, 0, 0.8);
    color: #fff;
    border-radius: 2px;
    z-index: 1;
  }
</style>
