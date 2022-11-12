import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { PacienteService } from 'src/app/services/paciente.service';
import { UsuarioService } from 'src/app/services/usuario.service';
import { UtilsService } from 'src/app/services/utils.service';

@Component({
  selector: 'app-actualizar-datos-personales',
  templateUrl: './actualizar-datos-personales.component.html',
  styleUrls: ['./actualizar-datos-personales.component.css']
})
export class ActualizarDatosPersonalesComponent implements OnInit {
  paciente: any = {};
  constructor(
    private _pacienteService: PacienteService,
    private _router: Router,
    private _utilsService: UtilsService
  ) {}

  ngOnInit(): void {
    let permission = localStorage.getItem("permission");
    if(permission == "0"){
      let data: any = localStorage.getItem("data")
      let jsonData = JSON.parse(data);
      this._pacienteService.obtenerPacientePorId(jsonData.id).subscribe(
        (res) => {
          
          this.paciente = res;
          console.log(this.paciente);
        },
        (err) => {
          this._utilsService.openSnackBarError("Error al obtener los datos del paciente");
        }
      )
    }
  }
  createCustomer(){
    if(
      this.paciente.nombres &&
      this.paciente.apellidos &&
      this.paciente.telefono &&
      this.paciente.genero &&
      this.paciente.direccion &&
      this.paciente.ciudad &&
      this.paciente.fecha_de_nacimiento
    ){
      this._pacienteService.actualizarPaciente(this.paciente, this.paciente.id).subscribe(
        (res) => {
          this._router.navigate(['/welcome'])
          this._utilsService.openSnackBarSuccessfully("Datos de paciente actualizados exitosamente");
        },
        (err) => {
          this._utilsService.openSnackBarError(err);
        }
      );
    }
    else
    {
      this._utilsService.openSnackBarError("Todos los campos son obligatorios")
    }
  }
}
