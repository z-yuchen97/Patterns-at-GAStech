# Vue.js Instructions

## 1 Develop on Local Machine
### 1.1 Install Vue-cli and Node_Modules
``` bash
$ npm install -g vue-cli
$ vue init webpack frontend
$ cd frontend
$ npm install
$ npm run dev
```
### 1.2 Cross-Domain Request
* Find in "build/webpack.dev.conf.js"
* Need to look into "/config/index.js" to modify config
* Modify proxy-table as:
``` javascript
proxyTable: {
      '/api': {
        target: 'http://localhost:5000',
        pathRewrite: {'^/api': ''}
      }
    }
```
* Hence, all of request from frontend to backend will via "api/..." url

## 2 Build on Server
``` bash
$ cd frontend
$ npm install
$ npm run build 
# help you generate a dist directory in frontend
$ cp -r dist/ /var/www/html
# you may want to rename the 'dist' directory for production mode
```
For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).