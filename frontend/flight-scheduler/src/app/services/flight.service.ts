import { Injectable } from '@angular/core';
import { HttpClient} from "@angular/common/http";
import { Observable } from "rxjs";
import { Flight } from "../models/flight";


@Injectable({
  providedIn: 'root'
})
export class FlightService {
  private endpoint='http://127.0.0.1:8000/flights/';
  constructor( private http:HttpClient ) { } 

  //GET ONE FLIGTH
  getFlight(id: number):Observable<any>{
    console.log("Entramos ")
    return this.http.get(this.endpoint + id)
  }

  //GET ALL FLIGHTS
  getAllFlights(): Observable<any>{
    return this.http.get(this.endpoint)
  }

  //Post Add new flight
  flightCreate(flight: Flight):Observable<object>{
    return this.http.post(this.endpoint,flight);
  }

  // PUT Update 
  updateFlight(id: number,payload:any):Observable<object>{
    return this.http.put(this.endpoint + id , payload); 
  }

  //delete a flight
  deleteFlight(id:number):Observable<any>{
    return this.http.delete(this.endpoint + id)
  }

  //delete all flights
  deleteAllFlights():Observable<any>{
    return this.http.delete(this.endpoint)

  }

}
