import React, { Component } from 'react';
import './App.css';
import 'whatwg-fetch'
class App extends Component {

  constructor(props){
      super(props);
      this.state ={
        mode: 'cors',
        data : {}
      }
  }

  fetch_data(){
    const BASE_URL = "http://0.0.0.0:5050/basicServer/services/giveJson";

    fetch(BASE_URL, {
      method: 'GET',
      // mode: this.state.mode,
      // headers:{
      //   'Access-Control-Allow-Origin':'*',
      //   'Access-Control-Allow-Credentials': true,
      //   body:null,
      // },
      mode: this.state.mode,
      body:null,
    })
    .then(response => response.json()) //json => this.setState(this.state.data: json)
    .then(json => {
      var data  = json['data'];
      console.log(json['data']);
      this.setState({data:data});
      console.log("State",this.state.data);
    });
  }

  componentWillMount() {
    this.fetch_data();
  }

  render() {

    return (
      <div className="App">
        <div className="App-header">
          <h2>Welcome to React</h2>
          <div>
            {this.state.data[10]}

          </div>
        </div>
      </div>
    );
  }
}

export default App;
