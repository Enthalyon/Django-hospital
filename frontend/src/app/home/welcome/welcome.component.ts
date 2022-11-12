import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.component.html',
  styleUrls: ['./welcome.component.css']
})
export class WelcomeComponent implements OnInit {
  data: any = {};
  stringData: any = "";
  role: any = { name: ""};
  rolesList: any[] = []
  constructor() { 
  }

  ngOnInit(): void {
    this.rolesList = [
      {name: 'Paciente', value: 0},
      {name: 'Personal de Salud', value: 1}, 
      {name: 'Familiar', value: 2}, 
      {name: 'Auxiliar', value: 3}
    ]
    this.stringData = localStorage.getItem("data");
    this.data = JSON.parse(this.stringData);
    let roleNumber = localStorage.getItem("permission");
    this.role = this.rolesList.filter((r: any) => r.value == roleNumber)[0]    
  }

}
