import { DroppedOrderReport } from './../dropped-order-report';
import { CompletedOrderReport } from './../completed-order-report';
import { HttpService } from './http.service';
import { Observable } from 'rxjs';

export interface HttpService {

    fetchCompletedOrderReport(): Observable<CompletedOrderReport>;
    fetchDroppedOrderReport(): Observable<DroppedOrderReport>;
}
