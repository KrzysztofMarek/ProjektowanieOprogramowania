import { Injectable } from '@angular/core';
import { Headers, RequestOptions, Response } from '@angular/http';
import { HttpClient } from '@angular/common/http';
import { Recruitment } from '../models/Recruitment';

@Injectable()
export class DataService {

    constructor(public http: HttpClient) { }

    id:string; 

    getRecruitmentsList() {
        return this.http.get('http://localhost:9090/pobierz_ogloszenia');
    }
}
