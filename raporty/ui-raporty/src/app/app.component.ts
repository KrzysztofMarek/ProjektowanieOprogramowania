import { AvgRealisationTimesReport } from './avg-realisation-times-report';
import { AvgDeliveryTimesReport } from './avg-delivery-times-report';
import { DroppedOrderReport } from './dropped-order-report';
import { HttpServiceImpl } from './services/http.service.impl';
import { Component, OnInit } from '@angular/core';
import { CompletedOrderReport } from './completed-order-report';
import { saveAs } from 'file-saver/FileSaver';

declare global {
  interface Window { html2canvas: any; }
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  dataDisplayed: any;
  currentType = 'none';
  diagramTypeChart = true;
  dataCompleted: CompletedOrderReport;
  dataDropped: DroppedOrderReport;
  dataAvgDelivery: AvgDeliveryTimesReport;
  dataAvgRealisation: AvgRealisationTimesReport;
  isUserLogged = false;

  constructor(private httpService: HttpServiceImpl) {}

  ngOnInit() {
    this.login();
  }

  login() {
    this.httpService.performLogin().subscribe(
      data => {
        this.isUserLogged = data;
      }
    );
  }

  completed() {
    this.httpService.fetchCompletedOrderReport().subscribe(
      data => {

        this.dataCompleted = data;
        this.currentType = 'completed';
        this.diagramTypeChart = true;

        const labelsFromData: string[] = [];

        data.nodes.forEach(d => {

          labelsFromData.push(d.restaurant);
        });

        const dataFromData: number[] = [];

        data.nodes.forEach(d => {

          dataFromData.push(d.completedOrders);
        });

        this.dataDisplayed = {
          labels: labelsFromData,
          datasets: [{
            data: dataFromData,
            backgroundColor: [
              '#ffccff',
              '#99ff99',
              '#ffff99'
            ]
          }]
        };
      }
    );
  }

  dropped() {
    this.httpService.fetchDroppedOrderReport().subscribe(
      data => {

        this.dataDropped = data;
        this.currentType = 'dropped';
        this.diagramTypeChart = true;

        const labelsFromData: string[] = [];

        data.nodes.forEach(d => {

          labelsFromData.push(d.restaurant);
        });

        const dataFromData: number[] = [];

        data.nodes.forEach(d => {

          dataFromData.push(d.droppedOrders);
        });

        this.dataDisplayed = {
          labels: labelsFromData,
          datasets: [{
            data: dataFromData,
            backgroundColor: [
              '#ffccff',
              '#99ff99',
              '#ffff99'
            ]
          }]
        };
      }
    );
  }

  avgDeliveries() {

    this.httpService.fetchAvgDeliveryTimes().subscribe(
      data => {

        this.dataAvgDelivery = data;
        this.currentType = 'avgDelivery';
        this.diagramTypeChart = false;

        const labelsFromData: string[] = [];

        data.nodes.forEach(d => {

          labelsFromData.push(d.city);
        });

        const dataFromData: number[] = [];

        data.nodes.forEach(d => {

          dataFromData.push(d.averageDeliveryTime);
        });

        this.dataDisplayed = {
          labels: labelsFromData,
          datasets: [{
            data: dataFromData,
            backgroundColor: [
              '#ffccff',
              '#99ff99',
              '#ffff99'
            ]
          }]
        };
      }
    );
  }

  avgRealisations() {

    this.httpService.fetchAvgRealisations().subscribe(
      data => {

        this.dataAvgRealisation = data;
        this.currentType = 'avgRealisation';
        this.diagramTypeChart = false;

        const labelsFromData: string[] = [];

        data.nodes.forEach(d => {

          labelsFromData.push(d.city);
        });

        const dataFromData: number[] = [];

        data.nodes.forEach(d => {

          dataFromData.push(d.averageRealisationTime);
        });

        this.dataDisplayed = {
          labels: labelsFromData,
          datasets: [{
            data: dataFromData,
            backgroundColor: [
              '#ffccff',
              '#99ff99',
              '#ffff99'
            ]
          }]
        };
      }
    );
  }

  testReport(reportType) {

    if (reportType === 'none') {

      throw new Error('No data to report!');

    } else if (reportType === 'completed') {

      this.httpService.fetchCompletedOrderReportAsPdf().subscribe(
        (response: Response) => {
          const blob = new Blob([response], {type: 'application/pdf'});
          saveAs(blob, 'report.pdf');
        }
      );

    } else if (reportType === 'dropped') {

      this.httpService.fetchDroppedOrderReportAsPdf().subscribe(
        (response: Response) => {
          const blob = new Blob([response], {type: 'application/pdf'});
          saveAs(blob, 'report.pdf');
        }
      );

    } else if (reportType === 'avgDelivery') {

      this.httpService.fetchAvgDeliveryTimesAsPdf().subscribe(
        (response: Response) => {
          const blob = new Blob([response], {type: 'application/pdf'});
          saveAs(blob, 'report.pdf');
        }
      );

    } else if (reportType === 'avgRealisation') {

      this.httpService.fetchAvgRealisationsAsPdf().subscribe(
        (response: Response) => {
          const blob = new Blob([response], {type: 'application/pdf'});
          saveAs(blob, 'report.pdf');
        }
      );
    }
  }
}
