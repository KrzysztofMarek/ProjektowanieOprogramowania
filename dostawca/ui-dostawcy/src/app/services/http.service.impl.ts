import { OrderWithContact } from './../order-with-contact';
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

  fetchOrders(): Observable<OrderWithContact[]> {

    return this.http.get<OrderWithContact[]>(
      'http://localhost:8080/delivery/orderList/1'
    );
  }

  changeOrderStatus(id, status): Observable<OrderWithContact[]> {

    return this.http.get<OrderWithContact[]>(
      'http://localhost:8080/delivery/' + id + '/' + status + '/1'
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
