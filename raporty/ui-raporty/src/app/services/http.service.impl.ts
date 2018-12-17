import { Histogram } from './../histogram';
import { AvgRealisationTimesReport } from './../avg-realisation-times-report';
import { AvgDeliveryTimesReport } from './../avg-delivery-times-report';
import { DroppedOrderReport } from './../dropped-order-report';
import { CompletedOrderReport } from './../completed-order-report';
import { HttpService } from './http.service';
import { Injectable } from '@angular/core';
import { Observable, from } from 'rxjs';
import { map } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpServiceImpl implements HttpService {

  private headers = new HttpHeaders();

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

  constructor(private http: HttpClient) {
    this.headers.append('Content-Type', 'application/pdf');
  }

  fetchCompletedOrderReport(): Observable<CompletedOrderReport> {

    return this.http.get<CompletedOrderReport>(
      'http://localhost:8081/fetch-completed-order-report'
    );
  }


  fetchDroppedOrderReport(): Observable<DroppedOrderReport> {

    return this.http.get<DroppedOrderReport>(
      'http://localhost:8081/fetch-dropped-order-report'
    );
  }

  fetchAvgDeliveryTimes(): Observable<AvgDeliveryTimesReport> {

    return this.http.get<AvgDeliveryTimesReport>(
      'http://localhost:8081/fetch-average-delivery-time'
    );
  }

  fetchAvgRealisations(): Observable<AvgRealisationTimesReport> {

    return this.http.get<AvgRealisationTimesReport>(
      'http://localhost:8081/fetch-average-realisation-time'
    );
  }

  fetchHistogram(): Observable<Histogram> {

    return this.http.get<Histogram>(
      'http://localhost:8081/fetch-histogram'
    );
  }

  fetchHistogramAsPdf(): any {

    return this.http.get(
      'http://localhost:8081/fetch-histogram',
      {headers: this.headers, responseType: 'blob'}
    );
  }

  fetchCompletedOrderReportAsPdf(): any {

    return this.http.get(
      'http://localhost:8081/create-completed-order-report-pdf',
      {headers: this.headers, responseType: 'blob'}
    );
  }


  fetchDroppedOrderReportAsPdf(): any {

    return this.http.get(
      'http://localhost:8081/create-dropped-order-report-pdf',
      {headers: this.headers, responseType: 'blob'}
    );
  }

  fetchAvgDeliveryTimesAsPdf(): any {

    return this.http.get(
      'http://localhost:8081/create-average-delivery-time-pdf',
      {headers: this.headers, responseType: 'blob'}
    );
  }

  fetchAvgRealisationsAsPdf(): any {

    return this.http.get(
      'http://localhost:8081/create-average-realisation-time-pdf',
      {headers: this.headers, responseType: 'blob'}
    );
  }
}
