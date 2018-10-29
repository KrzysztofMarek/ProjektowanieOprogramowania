import { Order } from './order';
import { HttpServiceImpl } from './services/http.service.impl';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  orderList: Order[];
  currentOrder: Order;

  constructor(private httpService: HttpServiceImpl) { }

  ngOnInit() {
    this.currentOrder = null;
    this.httpService.fetchOrders().subscribe(
      data => {
        this.orderList = data;
      }
    );
  }

  takeOrder(id) {
    this.currentOrder = this.orderList.filter(o => o.id === id)[0];
    this.httpService.changeOrderStatus(this.currentOrder.id, 'INPREPARATION').subscribe(
      data => {
        this.orderList = data;
      }
    );
  }

  finalizeRealisation() {
    this.httpService.changeOrderStatus(this.currentOrder.id, 'ONTHEWAY').subscribe(
      data => {
        this.orderList = data;
      }
    );
    this.currentOrder = null;
  }

  dropCurrentOrder() {
    this.httpService.changeOrderStatus(this.currentOrder.id, 'WAITING').subscribe(
      data => {
        this.orderList = data;
      }
    );
    this.currentOrder = null;
  }

  getCoursesList(order): string {

    if (order !== null) {
      let list = '';
      const coursesNames = order.courseList.map(o => o.name);
      coursesNames.forEach(c => {
        list = list + c + ', ';
      });
      return list.substring(0, list.length - 2);
    } else {
      return '';
    }
  }
}
