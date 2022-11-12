import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  roleNumber: any;
  constructor() { }

  ngOnInit(): void {
  }

  tokenExist(){
    let token = localStorage.getItem("token");
    return token == undefined ? true : false;
  }
  esAuxiliar(){
    return parseInt(localStorage.getItem("permission") ?? "-1") == 3 ? true : false;
  }

  esPaciente(){
    return parseInt(localStorage.getItem("permission") ?? "-1") == 0 ? true : false;
  }

  esProfesional(){
    return parseInt(localStorage.getItem("permission") ?? "-1") == 1 ? true : false;
  }

  esFamiliar(){
    return parseInt(localStorage.getItem("permission") ?? "-1") == 2 ? true : false;
  }

  salir(){
    localStorage.clear();
  }
}
