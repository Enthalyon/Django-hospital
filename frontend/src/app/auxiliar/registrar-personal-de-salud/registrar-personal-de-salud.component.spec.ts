import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistrarPersonalDeSaludComponent } from './registrar-personal-de-salud.component';

describe('RegistrarPersonalDeSaludComponent', () => {
  let component: RegistrarPersonalDeSaludComponent;
  let fixture: ComponentFixture<RegistrarPersonalDeSaludComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegistrarPersonalDeSaludComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RegistrarPersonalDeSaludComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
