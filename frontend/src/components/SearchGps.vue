<template>
  <div>
    <div id = "headimg">
      <img width="400px" height="100px"  src = "../../static/img/Kronos.jpg">
    </div>
    <div id = "navigate">
      <input type="button" class = "btn" value="Background Story" @click="showdialog" />
      <div id="mydialog" title="Background Story">
        {{guide_text.para1}}<br><br>
        {{guide_text.para2}}<br><br>
        {{guide_text.para3}}<br><br>
        {{guide_text.para4}}<br><br>
      </div>
      <input type="button" class = "btn" value="Task" @click="showtask" />
      <div id="mytask" title="Task">
        {{guide_text.task1}}<br><br>
        {{guide_text.task2}}<br><br>
      </div>
      <button class = "btn" style="color:black;" @click="showvideo">Video Link</button>
      <a href = "http://52.14.238.110/kronos"> <button class = "btn" style="color:black;">13 Inch Interface</button></a>
    </div>
    <div id = "control">
      <input type="button" id = "start" class = "btn" value="Start Logging" @click="record_start" />
      <input type="button" id = "stop" class = "btn" value="Stop Logging" @click="record_cancel" />
    </div>
    <div id = "slide">
      <b>Point Speed</b>: &nbsp;Fast x 10&nbsp;&nbsp;<input v-model="coefficient" type="range" min="10" max="500" value="100" class="slider" id="myRange">&nbsp;&nbsp;Slow x 5
    </div>
    <div id="search">
      <!-- <div id="name-search">
        <strong>Name:</strong>
        <select v-model="name" class="select" style="width:120px;">
            <option disabled value selected>--Name--</option>
            <option>All Employee</option>
            <option>Truck Drivers</option>
            <option v-for="(pinfo, index) in personal_info" :key="index">{{pinfo.firstname}} {{pinfo.lastname}}</option>
        </select>
      </div> -->
      <div id="time-search" >
        <strong>From:</strong>
        <select v-model="start_date" class="time soption" style="width:70px;">
          <option disabled value selected>-date-</option>
          <option v-for="(d, index) in time_info.date" :key="index">{{d}}</option>
        </select>
        <select v-model="start_hour" class="time soption" style="width:70px;">
          <option disabled value selected>-hour-</option>
          <option v-for="(h, index) in time_info.hour" :key="index">{{h}}</option>
        </select>
        <select v-model="start_minute" class="time soption" style="width:90px;">
          <option disabled value selected>-minute-</option>
          <option v-for="(m, index) in time_info.minute" :key="index">{{m}}</option>
        </select>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <strong>To:</strong>
        <select v-model="end_date" class="time soption" style="width:70px;">
          <option disabled value selected>-date-</option>
          <option v-for="(d, index) in time_info.date" :key="index">{{d}}</option>
        </select>
        <select v-model="end_hour" class="time soption" style="width:70px;">
          <option disabled value selected>-hour-</option>
          <option v-for="(h, index) in time_info.hour" :key="index">{{h}}</option>
        </select>
        <select v-model="end_minute" class="time soption" style="width:90px;">
          <option disabled value selected>-minute-</option>
          <option v-for="(m, index) in time_info.minute" :key="index">{{m}}</option>
        </select>
        <br>
        <br>
        <button class = "searchbtn" @click="searchRange">Search</button>
        <br>
        <i class="fa fa-spinner fa-spin" id = "loading" style ="display:none"></i>
      </div>
    </div>
    <div id="namebar">
      <p class = "namebox"><strong>Please Select Employee:</strong></p>
      <input class = "namebox" type="radio" name = "employee" v-model="name" value="All Employee">
      <label for="male">All Employee</label><br>
      <input class = "namebox" type="radio" name = "employee" v-model="name" value="Truck Drivers">
      <label for="male">Truck Drivers</label>
      <svg width="12" height="12"> 
        <rect width="12" height="12" style="fill: brown" />
      </svg>
      <br>
      <div v-for="(pinfo, index) in personal_info" :key="index" >
        <input class = "namebox" type="radio" name = "employee" v-model="name" v-bind:value="pinfo.firstname+' '+pinfo.lastname">
        <label >{{pinfo.firstname}} {{pinfo.lastname}}</label>
          <svg width="12" height="12"> 
            <rect width="12" height="12" v-bind:style="{fill: pinfo.color}" />
          </svg>
        <br>
      </div>
    </div>
    <div>
      <div id="personalpoint"></div>
      <div id="point"></div>
      <div id="map" :style="{backgroundImage: 'url(' + require('@/assets/MC2-tourist.jpg') + ')'}"></div>
    </div>
    <div id="trackbar">
      <table style="width:100%">
        <tr>
          <th colspan="1">
            <strong>Pause > 10 Minutes:</strong>
          </th>
        </tr>
        <tr v-for="(d, index) in pause_info" :key="index">
          <th>{{d}}</th>
        </tr>
      </table> 
    </div>
    <div id = "card">
      <!-- <ul>
        <li v-for="(d, index) in card_info" :key="index">{{d.type}} : {{d.location}}, 
          {{d.timestamp}}, {{d.price}}, {{d.name}}</li><br>
      </ul> -->
       <table style="width:100%">
        <tr>
          <th colspan="5">
            <strong>Creadit and Loyalty Card Data Information</strong>
          </th>
        </tr>
        <tr>
          <th>Type</th>
          <th>Location</th>
          <th>Time</th>
          <th>Price</th>
          <th>Name</th>
        </tr>
        <tr v-for="(d, index) in card_info" :key="index">
          <th>{{d.type}}</th>
          <th>{{d.location}}</th>
          <th>{{d.timestamp}}</th>
          <th>{{d.price}}</th>
          <th>{{d.name}}</th>
        </tr>
      </table> 
    </div>
    <div id = "histogram">
    </div>
    <div id = "wordcloud">
      <table style="width:100%">
        <tr>
          <th colspan="1">
            <strong>Words Cloud for Card Info(Bigger Font Sizes Means Higher Frequency):</strong>
          </th>
        </tr>
      </table>
    </div>
    <div id="productId" >
        <iframe allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true" width="600" height="380"
          src="https://www.youtube.com/embed/kvOvDXxF0uU">
        </iframe> 
    </div>
    <div id = "bottom">
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SearchGps",
  data() {
    return {
      circle: false,
      pause_info: [],
      record_log: false,
      record_set: [],
      personal_info: [],
      time_info: [],
      guide_text: "",
      gps_info: "",
      card_info: "",
      slot_info: "",
      dataset: [],
      name: "",
      firstname: "",
      lastname: "",
      start_date: "",
      start_hour: "",
      start_minute: "",
      end_date: "",
      end_hour: "",
      end_minute: "",
      coefficient: 100
    };
  },

  mounted() {

    // generate page when first load
    // axios.get("api/init_person")
    //       .then(response => (this.personal_info = response.data));
    // axios.get("api/init_time")
    axios.get("http://52.14.238.110:5000/init_person")
          .then(response => (this.personal_info = response.data));
    axios.get("http://52.14.238.110:5000/init_time")
          .then(response => (this.time_info = response.data));
    axios.get("http://52.14.238.110:5000/init_text")
          .then(response => (this.guide_text = response.data));
    axios.get("http://52.14.238.110:5000/init_color")
          .then(response => (this.color_info = response.data));
  },

  methods: {

    showvideo: function() {  
      const returnEle = document.querySelector("#productId");  
      if (!!returnEle) {
        returnEle.scrollIntoView(true); 
      }
      document.querySelector("showvideo").scrollIntoView(true); 
    },


    record_start: function(){
      this.record_log = true;
      document.getElementById("start").style.backgroundColor = "black";
      document.getElementById("start").style.color= "white";
      console.clear();
    },

    record_cancel: function(){
      this.record_log = false;
      document.getElementById("start").style.backgroundColor = "lightgray";
      document.getElementById("start").style.color= "black";
      for(let i=0; i<this.record_set.length; i++){
        console.log(this.record_set[i]);
      }
      this.record_set = [];
    },

    logdata: function(d, type){
      if(this.record_log == true){
        if (type == "mouseover"){
          let log = {name: d.firstname + " " + d.lastname,
          timestamp: d.timestamp,
          longtitude: d.longtitude,
          latitude: d.latitude};
          this.record_set.push(log);
        }else{
          let name = d.firstname + " " + d.lastname;
          console.log("chosen name:"+name);
        }
      }
    },

    showdialog: function(){
      $("#mydialog").dialog({
        width: "700"
      });
    },

    showtask: function(){
      $("#mytask").dialog({
        width: "700"
      });
    },

    searchTime: async function(d){
      let time1 = "14-1-" + start_date + " " + d.slot -2 + ":0";
      let time2 = "14-1-" + start_date + " " + d.slot + ":0";
      const res = await axios.get('http://52.14.238.110:5000/search_gps', {
        params: {
          firstname: "",
          lastname: "",
          time_start: time1,
          time_end: time2
          }
        }
      );
    },

    // async function to wait axios 
    searchRange: async function(){
      var x = document.getElementById("loading");
      if (x.style.display === "none") {
        x.style.display = "block";
      }
      console.log("search name: "+this.name);
      if(this.name == ""){
        alert("Please Select Employee.")
      }
      if(this.start_date == "" ||  this.start_hour == "" || this.start_minute == "" || this.end_date == "" ||this.end_hour == "" ||this.end_minute == ""){
        alert("Please Select Date!");
      }else{
        let start_sec = Number(this.start_date) * 1440 + Number(this.start_hour) * 60 + Number(this.start_minute);
        let end_sec = Number(this.end_date) * 1440 + Number(this.end_hour) * 60 + Number(this.end_minute);
        if ( Number(start_sec) >= Number(end_sec) ) {
          alert("Time Search Range is Invalid!");
        }else{
          let time_start = "14-1-" + this.start_date + " " + this.start_hour + ":" + this.start_minute
          let time_end = "14-1-" + this.end_date + " " + this.end_hour + ":" + this.end_minute
          console.log("time start" + time_start);
          console.log("time end" + time_end);
          let firstname;
          let lastname;
          if(this.name == "All Employee"){
            if( Number(end_sec) - Number(start_sec) >= 2400){
              return alert("Due to Micro AWS features, cannot support search beyond 40 hours! Sorry for this inconvenience!");
            }
            firstname = "";
            lastname = "";
        }else if(this.name == "Truck Drivers"){
          firstname = "Truck Drivers";
          lastname = "Truck Drivers";
        }else{
          firstname = this.name.split(' ', 1)[0];
          lastname = this.name.slice(this.name.indexOf(' ')+1);
        }
        const res = await axios.get('http://52.14.238.110:5000/search_gps', {
          params: {
            firstname: firstname,
            lastname: lastname,
            time_start: time_start,
            time_end: time_end
            }
          }
        );
        const res_card = await axios.get('http://52.14.238.110:5000/search_card', {
          params: {
            firstname: firstname,
            lastname: lastname,
            time_start: time_start,
            time_end: time_end
            }
          }
        );
        const res_date = await axios.get('http://52.14.238.110:5000/search_hist', {
          params: {
              time_start: time_start
            }
          }
        );
        // this.gps_info = JSON.stringify(res.data);
        if (x.style.display === "block") {
          x.style.display = "none";
        }
        this.gps_info = res.data;
        this.card_info = res_card.data;
        this.slot_info = res_date.data;
        let present = "1/" + this.start_date + "/2014";
        this.render();
        setTimeout(this.histplot, 3000, present, this.start_date);
        this.draw_word_cloud(this.card_info);
        }
      }
    },

    count_word: function(myWords){
      var countedWords = myWords.reduce(function (allWords, word) { 
        if (word in allWords) {
          allWords[word]++;
        }
        else {
          allWords[word] = 1;
        }
        return allWords;
      }, {});
      return countedWords;
    },


    draw_word_cloud: function(card_info){
      var delete_svg = document.getElementById("word")
      if(delete_svg != null){
        delete_svg.remove();
      }
      var location_word = [];
      for(let i= 0; i < card_info.length; i ++){
        location_word.push(card_info[i].location);
      }
      var myWords = location_word;
      var newWords = this.count_word(myWords);
      var sum_count = 0;

      var wordset = [];
      Object.keys(newWords).forEach(function(key){
        wordset.push({'word': key, 'size': newWords[key]})
      })

      var margin = {top: 20, right: 5, bottom: 10, left: 10};
      var cloud_width = 560 - margin.left - margin.right;
      var cloud_height = 370 - margin.top - margin.bottom;

      var svg = d3.select("#wordcloud").append("svg")
        .attr("width", cloud_width)
        .attr("height", cloud_height)
        .attr("id", "word")
        .append("g")
        .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");
    
      var layout = d3.layout.cloud()
        .size([cloud_width, cloud_height])
        .words(wordset.map(function(d) { return {text: d.word, size:d.size}; }))
        .padding(10)
        .fontSize(function(d) { return d.size; })
        .on("end", function(words){
          svg.append("g")
          .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
          .selectAll("text")
          .data(words)
          .enter().append("text")
          .style("font-size", function(d) {
            if(d.size < 10){
              return 20 + "px";
            }else if(d.size < 20){
              return 30 + "px";
            }else if(d.size < 30){
              return 40 + "px";
            }else{
              return 60 + "px";
            };
          })
          .style("fill", function(){
            return "hsl(" + Math.random() * 360 + ", 100%, 50%)";
          })
          .style("opacity", function(d){
            if(d.size < 10){
              return 0.5;
            }else if(d.size < 20){
              return 0.65;
            }else if(d.size < 30){
              return 0.9;
            }else{
              return 1;
            };
          })
          .attr("font-weight", "bold")
          .attr("text-anchor", "middle")
          .attr("transform", function(d) {
            return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
          })
          .text(function(d) { return d.text; });
        });
      layout.start();
    },


    histplot: function(present, start_date){
      var delete_svg = document.getElementById("hist")
      if(delete_svg != null){
        delete_svg.remove();
      }
      let histset = [];
      histset = this.slot_info;

      let tip = d3.tip()
        .attr('class', 'd3-tip')
        .offset([-20, 0])
        .html(function(d) {
                return "<div style = 'background-color:black; opacity:0.8; color: #fff;border-radius: 2px; " 
                + "font-weight: bold; padding: 2px;' > " 
                + "</span><br>GPS Tracks:<span style='color:white'>" + d.number + "</div>"
        })

      let title = present + " " + "GPS Track distribution"
      var margin = {top: 50, right: 40, bottom: 50, left: 60}
      var width = 600 - margin.left - margin.right;
      var height = 320 - margin.top - margin.bottom;
      var binwidth = width/12;

      var yScale = d3.scaleLinear()
        .domain([0, d3.max(histset, function(d,i){return d.number})])
        .range([height, 0]);
      var xScale = d3.scaleLinear()
        .domain([0, d3.max(histset, function(d,i){return d.slot})])
        .range([0, width]);

      var histogram = d3.histogram()
        .value(function(d) { return d.number; })   // I need to give the vector of value
        .domain(xScale.domain())  // then the domain of the graphic
        .thresholds(xScale.ticks(4)); // then the numbers of bins

      var svg = d3.select("#histogram")
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .attr("id", "hist")
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
      
      svg.call(tip);
      var bar = svg.selectAll(".bar")
        .data(histset)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .attr("x", function(d) { return xScale(d.slot-2); })
        .attr("width", binwidth)
        .attr("y", function(d) { return yScale(d.number); })
        .attr("height", function(d) { return height - yScale(d.number); })
        .on("mouseover", function(d){
          tip.show(d);
        })
        .on("mouseout", function(d){
          tip.hide(d);
        })
        .on("click", function(d){
          this.searchTime(d);
        })
        
      svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(xScale));
      svg.append("g")
        .call(d3.axisLeft(yScale));

      // Add axis labels
      svg.append("text")
          .attr("class", "x label")
          .attr("transform", "translate(" + (width / 2) + " ," + (height + margin.bottom - 15) + ")")
          //.attr("dy", "1em")
          .attr("text-anchor", "middle")
          .text("Every 2 hours");
          
      svg.append("text")
          .attr("class", "y label")
          .attr("transform", "rotate(-90)")
          .attr("y", 0 - margin.left)
          .attr("x", 0 - (height / 2))
          .attr("dy", "1em")
          .attr("text-anchor", "middle")
          .text("Count");
          
      // Add title to chart
      svg.append("text")
          .attr("class", "title")
          .attr("transform", "translate(" + (width / 2) + " ," + (-20) + ")")
          //.attr("dy", "1em")
          .attr("text-anchor", "middle")
          .style("fill", "#8A2BE2")
          .text(title);
    },


    sleep: function(ms){
      return new Promise(resolve => setTimeout(resolve, ms));
    },

    personal_render: async function(firstname, color){
      let control = this.coefficient / 100;
      console.log(control);
      let _this = this;
      let name = [];
      let middle = -1;
      let sleeptime = 7 * control;
      let randomColor = "brown"; // Truck Driver
      let j = 0;
      for(; j < this.personal_info.length; j ++){
        if(this.personal_info[j].firstname == firstname){
          randomColor = this.personal_info[j].color;
        }
      }
      name = document.getElementsByClassName(firstname);
      for(let i=0; i<name.length; i++){
        name[i].style.fill = randomColor;
        name[i].style.opacity = 1;
        name[i].setAttribute("float", "right");
        name[i].setAttribute("r", 5);
        await this.sleep(sleeptime);
        if(i == 0 || i == name.length -1){
          name[i].setAttribute("r", 10);
        }else{
          var old = new Date(name[i-1].getAttribute("time"));
          var present = new Date(name[i].getAttribute("time"));
          var diff = present - old;
          if(diff > 200000){
            if(middle > 0){
              name[middle].setAttribute("r", 1);
              _this.pause_info.push(present);
            }
            middle = i;
            sleeptime = 770;
            name[i].setAttribute("r", 10);
          }else{
            sleeptime = 7 * control;
            name[i].setAttribute("r", 1);
          }
        }
      }
    },

    render: function(){
      let _this = this;
      var delete_svg = document.getElementById("canvas")
      if(delete_svg != null){
        delete_svg.remove();
      }
      //Create SVG element
      let w = 960;
      let h = 480;
      let svg = d3.select("#point")
                  .append("svg")
                  .attr("width", w)
                  .attr("height", h)
                  .attr("id", "canvas");
      
      let tip = d3.tip()
        .attr('class', 'd3-tip')
        .offset([-10, 0])
        .html(function(d) {
                return "<div style = 'background-color:black; opacity:0.8; color: #fff;border-radius: 2px; " 
                + "line-height: 1;font-weight: bold; padding: 12px;' > " 
                + "<span style='color:violet'>" + d.firstname + " " + d.lastname 
                + "</span><br>TimeStamp:<span style='color:pink'>" + d.timestamp + "</div>"
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
      svg.selectAll("circle")
        .data(dataset)
        .enter()
        .append("circle")
        .attr('r', 1)
        .attr('cx', function(d) { return x(d['longtitude']) })
        .attr('cy', function(d) { return y(d['latitude']) })
        .attr("width", 2)
        .attr("height", 2)
        .attr("time", function(d){return d.timestamp})
        .attr("class", function(d){return d.firstname})
        .style('opacity', 0.3)
        .attr("fill", function(d, index){
          return "gray"
        })
        .attr("x", (d) => x(d.longtitude))
        .attr("y", (d) => y(d.latitude))
        .attr("stroke", "gray")
		    .attr("stroke-width", 0.1)
        .on('mouseover', function(d){
          d3.select(this)
          .attr("fill", "#1E90FF")
          .attr("r", 5)
          .style("opacity", 0.9);
          tip.show(d);
          _this.logdata(d, "mouseover");
        })
        .on('mouseout', function(d){
          d3.select(this)
          .attr("fill", "gray")
          .attr("r", 1);
          tip.hide(d);
        })
        .on('click', function(d){
          _this.personal_render(d.firstname);
          _this.logdata(d, "click");
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

.btn {
  background-color: lightgrey;
  font-size: 14px;
  border-radius: 4px;
  border: 0.5px solid black;
  padding: 3px 7px;
}

.searchbtn {
  background-color: lightgrey;
  font-size: 14px;
  border-radius: 4px;
  border: 0.5px solid black;
  padding: 3px 20px;
}

.soption {
  background-color: white;
  font-size: 14px;
  border-radius: 4px;
  border: 0.5px solid black;
  padding: 1px 7px;
}

.loader {
  position: absolute;
  top: 120px;
  border: 1px solid #f3f3f3;
  border-radius: 50%;
  border-top: 1px solid #3498db;
  width: 20px;
  height: 20px;
  -webkit-animation: spin 2s linear infinite; /* Safari */
  animation: spin 2s linear infinite;
}

#control {
  position: absolute;
  top: 40px;
  left: 75.5%;
}

#navigate {
  position: absolute;
  top: 40px;
  left: 5.5%;
}

#mydialog {
  display:none;
}

#mytask {
  display:none;
}


#headimg {
  position: relative;
  text-align: center;
  margin: auto;
  top: -50px;
}


#search {
  top: -30px;
  position: relative;
  height: 60px;
  text-align: center;
}

.namebox {
  margin-left: 5px;
}

#namebar {
  top: 240px;
  position: absolute;
  left: 5%;
  height: 480px;
  width: 11%;
  overflow: auto;
  border: 1px solid black;
  border-radius: 2px;
}

#trackbar {
  top: 240px;
  position: absolute;
  right: 5%;
  height: 480px;
  width: 11%;
  overflow: auto;
  border: 1px solid black;
  border-radius: 2px;
}

#slide {
  left: 6%;
  position: absolute;
  top: 200px;
  /* z-index: 0; */
}


#map {
  background-size: 955px 510px;
  background-repeat: no-repeat;
  opacity: 0.7;
  width: 960px;
  height: 560px;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  position: absolute;
  top: 230px;
  z-index: -1;
}

#point {
  width: 960px;
  height: 480px;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  position: absolute;
  top: 230px;
  z-index: 0;
}

#personalpoint {
  width: 960px;
  height: 480px;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  position: absolute;
  top: 230px;
  z-index: 0;
}

#card {
  position: absolute;
  right: 12%;
  height: 320px;
  top: 780px;
  width: 550px;
  overflow: auto;
  border: 1px solid black;
  border-radius: 2px;
  font-size: 12px;
}

#histogram {
  position: absolute;
  height: 320px;
  top: 780px;
  width: 600px;
  border: 1px solid black;
  border-radius: 2px;
  left: 12%;
  /* font-size: 12px; */
}

#wordcloud {
  position: absolute;
  right: 12%;
  height: 380px;
  top: 1140px;
  width: 550px;
  overflow: auto;
  border: 1px solid black;
  border-radius: 2px;
  font-size: 12px;
}

#productId {
  position: absolute;
  left: 12%;
  top: 1140px;
}

#bottom {
  position: absolute;
  height: 20px;
  width: 200px;
  top: 1000px;
}

.d3-tip {
    line-height: 1;
    font-weight: bold;
    padding: 12px;
} 

</style>
