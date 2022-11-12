import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ProfesionalService } from 'src/app/services/profesional.service';
import { UsuarioService } from 'src/app/services/usuario.service';
import { UtilsService } from 'src/app/services/utils.service';

@Component({
  selector: 'app-registrar-personal-de-salud',
  templateUrl: './registrar-personal-de-salud.component.html',
  styleUrls: ['./registrar-personal-de-salud.component.css']
})
export class RegistrarPersonalDeSaludComponent implements OnInit {
  profesional: any ={};
  constructor(
    private _profesionalService: ProfesionalService,
    private _usuarioService: UsuarioService,
    private _router: Router,
    private _utilsService: UtilsService
  ) { }

  ngOnInit(): void {}
  createCustomer(){
    if(
      this.profesional.nombres &&
      this.profesional.apellidos &&
      this.profesional.telefono &&
      this.profesional.genero &&
      this.profesional.direccion &&
      this.profesional.especialidad &&
      this.profesional.es_medico != undefined &&
      this.profesional.email &&
      this.profesional.password
    ){
      
      this._usuarioService.crearUsuario(this.profesional).subscribe(
        (res) =>{
          this.profesional.id_usuario = res.id;
          this._profesionalService.crearProfesional(this.profesional).subscribe(
            (res) => {
              this._router.navigate(['/welcome'])
              this._utilsService.openSnackBarSuccessfully("profesional creado exitosamente");
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
