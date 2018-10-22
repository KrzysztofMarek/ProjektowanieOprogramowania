import { Order } from './../order';
import { Injectable } from '@angular/core';
import { Observable } from '../../../node_modules/rxjs';
import { HttpClient } from '../../../node_modules/@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private http: HttpClient) { }

  fetchOrders(): Observable<Order[]> {

    return this.http.get<Order[]>(
      'http://localhost:8080/orderList'
    );
  }
}
