import { DroppedOrderReport } from './dropped-order-report';
import { HttpServiceImpl } from './services/http.service.impl';
import { Component, OnInit } from '@angular/core';
import { CompletedOrderReport } from './completed-order-report';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  dataDisplayed: any;

  constructor(private httpService: HttpServiceImpl) { }

  ngOnInit() { }

  completed() {
    this.httpService.fetchCompletedOrderReport().subscribe(
      data => {

        const labelsFromData: string[] = [];

        data.nodes.forEach( d => {

          labelsFromData.push(d.restaurant);
        });

        const dataFromData: number[] = [];

        data.nodes.forEach( d => {

          dataFromData.push(d.completedOrders);
        });

        this.dataDisplayed = {
          labels: labelsFromData,
          datasets: [{
            data: dataFromData
          }]
        };
      }
    );
  }

  dropped() {
    this.httpService.fetchDroppedOrderReport().subscribe(
      data => {

        const labelsFromData: string[] = [];

        data.nodes.forEach( d => {

          labelsFromData.push(d.restaurant);
        });

        const dataFromData: number[] = [];

        data.nodes.forEach( d => {

          dataFromData.push(d.droppedOrders);
        });

        this.dataDisplayed = {
          labels: labelsFromData,
          datasets: [{
            data: dataFromData
          }]
        };
      }
    );
  }
}
