import { Component, OnInit } from '@angular/core';
import { Flight } from "../models/flight";
import { FlightService } from "../services/flight.service";
@Component({
  selector: 'app-flight-create',
  templateUrl: './flight-create.component.html',
  styleUrls: ['./flight-create.component.css']
})
export class FlightCreateComponent implements OnInit {

  flight: Flight = new Flight();
  success: boolean= false;
  trip_types = ["One Way","Round Trip","Multiple Destinations"];
  constructor(private flightservice: FlightService) { }

  ngOnInit(): void {
    
  }

  onSubmit(){
    this.saveFlight();
  }

  saveFlight(){
    this.flightservice.flightCreate(this.flight)
    .subscribe(
      data=>{
        this.success = true;
        console.log("new flight added")
      },
      error => console.log("error " + error)
      )
  }

}
