import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { PacienteService } from 'src/app/services/paciente.service';
import { SignosVitalesService } from 'src/app/services/signos-vitales.service';
import { UtilsService } from 'src/app/services/utils.service';

@Component({
  selector: 'app-crear-registro-signos-vitales',
  templateUrl: './crear-registro-signos-vitales.component.html',
  styleUrls: ['./crear-registro-signos-vitales.component.css']
})
export class CrearRegistroSignosVitalesComponent implements OnInit {
  signos: any = {};
  constructor(
    private _signosService: SignosVitalesService,
    private _pacienteService: PacienteService,
    private _activeRoute: ActivatedRoute,
    private _router: Router,
    private _utilsService: UtilsService
  ) {}

  ngOnInit(): void {
    let permission = localStorage.getItem("permission");
    if(permission == "0"){
      let data: any = localStorage.getItem("data")
      let jsonData = JSON.parse(data);
      this.signos.nombres = jsonData.nombres
      this.signos.id_paciente = jsonData.id
    }
    else if(permission == "2"){
      
      this._pacienteService.obtenerPacientePorId(this._activeRoute.snapshot.params.id).subscribe(
        (res) => {
          this.signos.nombres = res.nombres
          this.signos.id_paciente = res.id
        },
        (err) => {
          this._utilsService.openSnackBarError("Error al obtenerlos datos del paciente");
        }
      )
    }
    
  }
  crearSignos(){
    if(
      this.signos.id_paciente &&
      this.signos.oximetria &&
      this.signos.temperatura &&
      this.signos.frecuencia_respiratoria &&
      this.signos.glicemia
    ){
      this._signosService.crearSignos(this.signos).subscribe(
        (res) => {
          this._router.navigate(['/welcome'])
          this._utilsService.openSnackBarSuccessfully("Signos registrados exitosamente");
        },
        (err) => {
          this._utilsService.openSnackBarError("Error al registrar los signos del paciente");
        }
      );
    }
    else
    {
      this._utilsService.openSnackBarError("Todos los campos son obligatorios")
    }
  }
}
