import { Order } from './order';
import { HttpService } from './services/http.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  orderList: Order[];
  currentOrder: Order;

  constructor(private httpService: HttpService) {}

  ngOnInit() {
    this.httpService.fetchOrders().subscribe(
      data => {
        this.orderList = data;
        console.log(this.orderList);
      }
    );
  }

  takeOrder(id) {
    console.log(id);
  }
}
