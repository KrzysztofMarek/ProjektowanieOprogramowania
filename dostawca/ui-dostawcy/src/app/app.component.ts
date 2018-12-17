import { OrderWithContact } from './order-with-contact';
import { Order } from './order';
import { HttpServiceImpl } from './services/http.service.impl';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  orderList: OrderWithContact[];
  isUserLogged = false;

  constructor(private httpService: HttpServiceImpl) { }

  ngOnInit() {
    this.login();
    this.httpService.fetchOrders().subscribe(
      data => {
        this.orderList = data.filter( d => d.order.orderStatus !== 'dostarczono');
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

  deliver(id) {
    this.httpService.changeOrderStatus(id, 'dostarczono').subscribe(
      data => {
        this.orderList = data.filter( d => d.order.orderStatus !== 'dostarczono');
      }
    );
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