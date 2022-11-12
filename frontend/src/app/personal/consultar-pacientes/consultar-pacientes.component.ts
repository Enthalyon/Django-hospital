import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { PacienteService } from 'src/app/services/paciente.service';
import { ProfesionalService } from 'src/app/services/profesional.service';
import { SignosVitalesService } from 'src/app/services/signos-vitales.service';
import { UtilsService } from 'src/app/services/utils.service';

@Component({
  selector: 'app-consultar-pacientes',
  templateUrl: './consultar-pacientes.component.html',
  styleUrls: ['./consultar-pacientes.component.css'],
})
export class ConsultarPacientesComponent implements OnInit {
  pacientes: any = [];
  profesionales: any = [];
  constructor(
    private _pacienteService: PacienteService,
    private _profesionalService: ProfesionalService,
    private _utilsService: UtilsService,
    private _router: Router
  ) {}

  ngOnInit(): void {
    let permission = localStorage.getItem("permission");
    let data: any = localStorage.getItem('data');
    let jsonData = JSON.parse(data);

    if(permission == "1"){
      this._pacienteService.obtenerPacientesPorProfesional(jsonData.id).subscribe(
        (res) => {
          console.log(res);
          this.pacientes = res;
        },
        (err) => {
          this._utilsService.openSnackBarError(
            'Error al obtener los datos del paciente'
          );
        }
      );
    }
    else if(permission == "2"){
      this._pacienteService.obtenerPacientesPorFamiliar(jsonData.id).subscribe(
        (res) => {
          console.log(res);
          this.pacientes = res;
        },
        (err) => {
          this._utilsService.openSnackBarError(
            'Error al obtener los datos del paciente'
          );
        }
      );
    }
    else if(permission == "3"){
      this._pacienteService.obtenerTodosLosPacientes().subscribe(
        (res) => {
          console.log(res);
          this.pacientes = res;
        },
        (err) => {
          this._utilsService.openSnackBarError(
            'Error al obtener los datos del paciente'
          );
        }
      );
      
    }
    this._profesionalService.listarProfesionales().subscribe(
      (res) => {
        this.profesionales = res;
      },
      (err) => {
        this._utilsService.openSnackBarError(
          'Error al obtener los datos de los profesionales'
        );
      }
    )
    
  }

  viewHistory(id: any) {
    this._router.navigate([`/paciente/consultar-historia/${id}`]);
  }
  registrarSignos(id: any) {
    this._router.navigate([`/paciente/crear-registro-signos-vitales/${id}`]);
  }
  esProfesional() {
    return parseInt(localStorage.getItem('permission') ?? '-1') == 1
      ? true
      : false;
  }
  asignarProfesional(id: any, data: any){
    this._pacienteService.actualizarPaciente(data, id).subscribe(
      (res) => {
        this._utilsService.openSnackBarSuccessfully(
          'Profesional asignado correctamente'
        );
      },
      (err) => {
        this._utilsService.openSnackBarError(
          'Error al asignar profesional'
        );
      }
    )
  }
  esFamiliar() {
    return parseInt(localStorage.getItem('permission') ?? '-1') == 2
      ? true
      : false;
  }
  esAuxiliar(){
    return parseInt(localStorage.getItem("permission") ?? "-1") == 3 ? true : false;
  }
}
