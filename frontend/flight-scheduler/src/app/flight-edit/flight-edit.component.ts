import { Component, OnInit } from '@angular/core';
import { Observable } from "rxjs";
import { Flight } from "../models/flight";
import { FlightService } from "../services/flight.service";
import { ActivatedRoute } from "@angular/router";

@Component({
  selector: 'app-flight-edit',
  templateUrl: './flight-edit.component.html',
  styleUrls: ['./flight-edit.component.css']
})
export class FlightEditComponent implements OnInit {
   
  flight: Observable<Flight>;
  flight_id: number;
  success: boolean = false;
  trip_types = ["One Way","Round Trip","Multiple Destinations"];

  constructor(private flightservice: FlightService,
              private activatedRoute: ActivatedRoute) { }

  ngOnInit(): void {
    this.activatedRoute.paramMap.subscribe(
      params=>{
        
        this.flight_id = Number(params.get("id"));
        console.log("id ", this.flight_id)
      }
    );
    console.log(this.loadFlightData())
    this.loadFlightData();
  }

  loadFlightData(){
    this.flightservice.getFlight(this.flight_id)
    .subscribe(
      data => {
        this.flight = data;
        console.log("Load data " , this.flight)
      }
    );
  }

  updateFlight(){
    this.flightservice.updateFlight(this.flight_id,this.flight)
    .subscribe(
      data=>{
        this.flight = data as Observable<Flight>;
        this.success= true;
      },
      error=>console.log("Opps Cannor update! "+ error)
    );
  
  }
  onSubmit(){
    this.updateFlight();
  }

}
