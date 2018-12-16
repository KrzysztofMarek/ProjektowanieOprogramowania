import { HttpService } from './http.service';
import { Order } from '../order';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpServiceImpl implements HttpService {

  constructor(private http: HttpClient) { }

  fetchOrders(): Observable<Order[]> {

    return this.http.get<Order[]>(
      'http://localhost:8080/orderList/1'
    );
  }

  changeOrderStatus(id, status): Observable<Order[]> {

    return this.http.get<Order[]>(
      'http://localhost:8080/orderStatus/' + id + '/' + status + '/1'
    );
  }

  performLogin(): Observable<boolean> {

    return this.http.get<String>(
      'http://localhost:7777/getsession'
    ).pipe(map(data => {
      if (data === 'Not logged in!') {
        return false;
      } else {
        return true;
      }
    }));
  }
}
