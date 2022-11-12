import { HttpInterceptor } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { UsuarioService } from './usuario.service';

@Injectable({
  providedIn: 'root'
})
export class TokenInterceptorService implements HttpInterceptor {
  constructor(private _usuarioService: UsuarioService) {}
  intercept(req: any, next: any) {
    const tokenReq = req.clone({
      setHeaders: {
        Authorization: 'Bearer ' + this._usuarioService.getToken(),
      },
    });
    return next.handle(tokenReq);
  }
}
