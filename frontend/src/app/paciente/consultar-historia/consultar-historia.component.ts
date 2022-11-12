import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { SignosVitalesService } from 'src/app/services/signos-vitales.service';
import { UtilsService } from 'src/app/services/utils.service';

@Component({
  selector: 'app-consultar-historia',
  templateUrl: './consultar-historia.component.html',
  styleUrls: ['./consultar-historia.component.css']
})
export class ConsultarHistoriaComponent implements OnInit {
  historial: any = [];
  constructor(
    private _signosService: SignosVitalesService,
    private _utilsService: UtilsService,
    private _activeRoute: ActivatedRoute) 
    { }
    
  ngOnInit(): void {
    let permission = localStorage.getItem("permission");
    if(permission == "0"){
      let data: any = localStorage.getItem("data")
      let jsonData = JSON.parse(data);
      this._signosService.consultarSignosPorPaciente(jsonData.id).subscribe(
        (res) => {
          console.log(res);          
          this.historial = res;
        },
        (err) => {
          this._utilsService.openSnackBarError("Error al obtener los datos del paciente");
        }
      )
    }
    else if(permission == "1"){
      console.log(this._activeRoute.snapshot.params.id);
      
      this._signosService.consultarSignosPorPaciente(this._activeRoute.snapshot.params.id).subscribe(
        (res) => {
          console.log(res);          
          this.historial = res;
        },
        (err) => {
          this._utilsService.openSnackBarError("Error al obtener los datos del paciente");
        }
      )
    }
    else if(permission == "2"){
      console.log(this._activeRoute.snapshot.params.id);
      
      this._signosService.consultarSignosPorPaciente(this._activeRoute.snapshot.params.id).subscribe(
        (res) => {
          console.log(res);          
          this.historial = res;
        },
        (err) => {
          this._utilsService.openSnackBarError("Error al obtener los datos del paciente");
        }
      )
    }
  }

  updateReview(id: any, historia: any){
    this._signosService.actualizarSignos(id, historia).subscribe(
      (res) => {
        this._utilsService.openSnackBarSuccessfully("Comentario actualizado con exito!");
      },
      (err) => {
        this._utilsService.openSnackBarError("Ocurrio un error al actualizar los comentarios");
      }
    )
  }

  esProfesional(){
    return parseInt(localStorage.getItem("permission") ?? "-1") == 1 ? true : false;
  }
}
