import { Injectable } from '@angular/core';
import { Headers, RequestOptions, Response } from '@angular/http';
import { HttpClient } from '@angular/common/http';
import { Payment } from '../models/Payment';
import { Status } from '../models/Status';

@Injectable()
export class DataService {

    constructor(public http: HttpClient) { }

    pay(payment: Payment) {
        payment.id_klienta = 1;
        payment.id_zamowienia = 1;
        payment.suma = 30;
        return this.http.post('localhost:9201/zaplac', payment).subscribe(res => console.log(res));
    }

    getSuccess() {
        return this.http.get('localhost:9093/success')
            .subscribe(res => console.log('res'));
    }

    getFailure() {
        return this.http.get('localhost:9093/failure')
        .subscribe(res => console.log('res'));
    }
}
