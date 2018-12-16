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
  isUserLogged = false;

  constructor(private httpService: HttpServiceImpl) { }

  ngOnInit() {
    this.login();
    this.currentOrder = null;
    this.httpService.fetchOrders().subscribe(
      data => {
        this.orderList = data;
      }
    );
  }

  login() {
    this.httpService.performLogin().subscribe(
      data => {
        this.isUserLogged = data;
      }
    );
  }

  takeOrder(id) {
    this.currentOrder = this.orderList.filter(o => o.id === id)[0];
    this.httpService.changeOrderStatus(this.currentOrder.id, 'przygotowywane').subscribe(
      data => {
        this.orderList = data;
      }
    );
  }

  finalizeRealisation() {
    this.httpService.changeOrderStatus(this.currentOrder.id, 'w_drodze').subscribe(
      data => {
        this.orderList = data;
      }
    );
    this.currentOrder = null;
  }

  dropCurrentOrder() {
    this.httpService.changeOrderStatus(this.currentOrder.id, 'oczekujace').subscribe(
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
