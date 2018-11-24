import { Component, OnInit } from '@angular/core';
import { Recruitment } from '../../models/Recruitment';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-add-recruitment',
  templateUrl: './add-recruitment.component.html',
  styleUrls: ['./add-recruitment.component.css']
})
export class AddRecruitmentComponent implements OnInit {

  recruitment: Recruitment = new Recruitment();
  recruitmentNew: Recruitment = new Recruitment();

  constructor(public dataService: DataService) {

  }

  ngOnInit() {
    this.dataService.getRecruitmentsList().subscribe(recruitment => {
      this.recruitment = recruitment;
      console.log(recruitment);
    });
  }

  onSubmit() {
    this.dataService.addRecruitment(this.recruitmentNew)
      .subscribe(res => {
        console.log(res);
        this.dataService.getRecruitmentsList().subscribe(recruitment => {
          this.recruitment = recruitment;
          console.log(recruitment);
        });
      });
  }

  onCancel() {

  }

}
