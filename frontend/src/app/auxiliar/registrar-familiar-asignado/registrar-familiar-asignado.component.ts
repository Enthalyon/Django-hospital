import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FamiliarAsignadoService } from 'src/app/services/familiar-asignado.service';
import { UsuarioService } from 'src/app/services/usuario.service';
import { UtilsService } from 'src/app/services/utils.service';

@Component({
  selector: 'app-registrar-familiar-asignado',
  templateUrl: './registrar-familiar-asignado.component.html',
  styleUrls: ['./registrar-familiar-asignado.component.css']
})
export class RegistrarFamiliarAsignadoComponent implements OnInit {
  familiar: any = {} 
  constructor(
    private _familiarService: FamiliarAsignadoService,
    private _usuarioService: UsuarioService,
    private _router: Router,
    private _utilsService: UtilsService
  ) { }

  ngOnInit(): void {}
  createCustomer(){
    if(
      this.familiar.nombres &&
      this.familiar.apellidos &&
      this.familiar.telefono &&
      this.familiar.genero &&
      this.familiar.direccion &&
      this.familiar.parentesco &&
      this.familiar.email &&
      this.familiar.password
    ){
      this._usuarioService.crearUsuario(this.familiar).subscribe(
        (res) =>{
          this.familiar.id_usuario = res.id;
          this._familiarService.crearFamiliar(this.familiar).subscribe(
            (res) => {
              this._router.navigate(['/welcome'])
              this._utilsService.openSnackBarSuccessfully("familiar creado exitosamente");
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
