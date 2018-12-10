import { AvgRealisationTimesReport } from './../avg-realisation-times-report';
import { AvgDeliveryTimesReport } from './../avg-delivery-times-report';
import { DroppedOrderReport } from './../dropped-order-report';
import { CompletedOrderReport } from './../completed-order-report';
import { HttpService } from './http.service';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpServiceImpl implements HttpService {

  constructor(private http: HttpClient) { }

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
}
