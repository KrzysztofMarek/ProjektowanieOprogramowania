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
  alertString: string = "";

  constructor(public dataService: DataService) {

  }

  ngOnInit() {
    this.dataService.getRecruitmentsList().subscribe(recruitment => {
      this.recruitment = recruitment;
      console.log(recruitment);
      console.log(this.recruitment);
    });
  }

  onSubmit() {
    this.dataService.addRecruitment(this.recruitmentNew)
      .subscribe(res => {
        var getValueArray = Object.values(res)
        this.alertString += getValueArray;
        alert(this.alertString.split(',').join(""));
        this.alertString = "";
        this.dataService.getRecruitmentsList().subscribe(recruitment => {
          this.recruitment = recruitment;
        });
      });
  }

  onCancel() {

  }

}
