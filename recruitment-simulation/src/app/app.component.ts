import { Component } from '@angular/core';
import { DataService } from './services/data.service';
import { Recruitment } from './models/Recruitment';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'payment-simulation';
  recruitment: any = new Recruitment();

  constructor(public dataService: DataService) { }
  ngOnInit() {
    this.dataService.getRecruitmentsList().subscribe(recruitment => {
      this.recruitment = recruitment;
    });
  }

}