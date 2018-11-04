import { Injectable } from '@angular/core';
import { Headers, RequestOptions, Response } from '@angular/http';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class DataService {

    constructor(public http: HttpClient) { }

    sendStatus(status) {
        console.log('wysłane');
        return this.http.post('urlForStatus', status);
    }
}
