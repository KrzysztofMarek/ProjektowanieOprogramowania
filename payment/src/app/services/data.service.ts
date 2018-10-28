import { Injectable } from '@angular/core';
import { Headers, RequestOptions, Response } from '@angular/http';
import { HttpClient } from '@angular/common/http';
import { Payment } from '../models/Payment';

@Injectable()
export class DataService {

    constructor(public http: HttpClient) { }

    pay(payment: Payment) {
        return this.http.post('localhost:9201/zaplac', payment)
    }
}
