import { HttpService } from './http.service';
import { Order } from '../order';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

export interface HttpService {

    fetchOrders(): Observable<Order[]>;
    changeOrderStatus(id, status): Observable<Order[]>;
    performLogin(): Observable<boolean>;
}
