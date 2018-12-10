import { AvgRealisationTimesReport } from './avg-realisation-times-report';
import { AvgDeliveryTimesReport } from './avg-delivery-times-report';
import { DroppedOrderReport } from './dropped-order-report';
import { HttpServiceImpl } from './services/http.service.impl';
import { Component, OnInit } from '@angular/core';
import { CompletedOrderReport } from './completed-order-report';
import * as jspdf from 'jspdf';
import * as html2canvas from 'html2canvas';
import * as ascii from 'ascii-json';

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

  constructor(private httpService: HttpServiceImpl) { }

  ngOnInit() { }

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

    const text: string[] = [];
    let i = 20;

    if (reportType === 'none') {

      throw new Error('No data to report!');

    } else if (reportType === 'completed') {

      this.dataCompleted.nodes.forEach(n => {
        let tmp = n.restaurant + ': ' + n.completedOrders;
        tmp = ascii.escapeNonAsciis(tmp);
        text.push(tmp);
      });

    } else if (reportType === 'dropped') {

      this.dataDropped.nodes.forEach(n => {
        let tmp = n.restaurant + ': ' + n.droppedOrders;
        tmp = ascii.escapeNonAsciis(tmp);
        text.push(n.restaurant + ': ' + n.droppedOrders);
      });

    } else if (reportType === 'avgDelivery') {

      this.dataAvgDelivery.nodes.forEach(n => {
        let tmp = n.city + ': ' + n.averageDeliveryTime;
        tmp = ascii.escapeNonAsciis(tmp);
        text.push(tmp);
      });

    } else if (reportType === 'avgRealisation') {

      this.dataAvgRealisation.nodes.forEach(n => {
        let tmp = n.city + ': ' + n.averageRealisationTime;
        tmp = ascii.escapeNonAsciis(tmp);
        text.push(tmp);
      });
    }

    window.html2canvas = html2canvas;
    const pdf = new jspdf('landscape');
    const canvas = document.querySelector('canvas');
    const image = canvas.toDataURL('image/png', 1.0);
    pdf.addImage(image, 'JPEG', 10, 10, 280, 150);
    text.forEach(t => {
      pdf.text(t, 20, i);
      i = i + 10;
    });
    pdf.save('report.pdf');
  }
}
