import { OrderWithContact } from './../order-with-contact';
import { HttpService } from './http.service';
import { Order } from '../order';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpServiceImpl implements HttpService {

  constructor(private http: HttpClient) { }

  fetchOrders(): Observable<OrderWithContact[]> {

    return this.http.get<OrderWithContact[]>(
      'http://localhost:8080/orderList/dlivery/1'
    );
  }

  changeOrderStatus(id, status): Observable<OrderWithContact[]> {

    return this.http.get<OrderWithContact[]>(
      'http://localhost:8080/orderStatus/' + id + '/' + status + '/1'
    );
  }
}
