import { Injectable } from '@angular/core';
import { Headers, RequestOptions, Response, Http } from '@angular/http';
import { HttpClient } from '@angular/common/http';
import { Payment } from '../models/Payment';

@Injectable()
export class DataService {

    constructor(
        public http: Http
    ) { }

    pay() {
    	window.open('https://stackoverflow.com', '_blank');
    }
}
