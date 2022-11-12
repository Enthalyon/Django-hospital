import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { PacienteService } from 'src/app/services/paciente.service';
import { UsuarioService } from 'src/app/services/usuario.service';
import { UtilsService } from 'src/app/services/utils.service';

@Component({
  selector: 'app-registrar-paciente',
  templateUrl: './registrar-paciente.component.html',
  styleUrls: ['./registrar-paciente.component.css']
})
export class RegistrarPacienteComponent implements OnInit {
  paciente: any = {};
  constructor(
    private _pacienteService: PacienteService,
    private _usuarioService: UsuarioService,
    private _router: Router,
    private _utilsService: UtilsService
  ) {}

  ngOnInit(): void {}
  createCustomer(){
    if(
      this.paciente.nombres &&
      this.paciente.apellidos &&
      this.paciente.telefono &&
      this.paciente.genero &&
      this.paciente.direccion &&
      this.paciente.ciudad &&
      this.paciente.fecha_de_nacimiento &&
      this.paciente.email &&
      this.paciente.password
    ){
      this._usuarioService.crearUsuario(this.paciente).subscribe(
        (res) =>{
          this.paciente.id_usuario = res.id;
          this._pacienteService.crearPaciente(this.paciente).subscribe(
            (res) => {
              this._router.navigate(['/welcome'])
              this._utilsService.openSnackBarSuccessfully("Paciente creado exitosamente");
            },
            (err) => {
              this._utilsService.openSnackBarError(err);
            }
          );
        },
        (error) => {
          this._utilsService.openSnackBarError("Ha ocurrido un error al registrar el usuario");
        }
      )
    }
    else
    {
      this._utilsService.openSnackBarError("Todos los campos son obligatorios")
    }
  }
}
