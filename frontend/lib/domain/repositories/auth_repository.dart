import 'package:dartz/dartz.dart';
import '../../core/errors/failures.dart';
import '../entities/user.dart';

abstract class AuthRepository {
  // login with email and password
  Future<Either<Failure, User>> login({
    required String email,
    required String password,
  });

  // register a new user
  Future<Either<Failure, User>> register ({
    required name,
    required email,
    required password,
    required passwordConfirmation,
  });

  // logout current user
  Future<Either<Failure, void>> logout();

  // check if logged in
  Future<bool> isLoggedIn();

  // get current user from storage
  Future<Either<Failure, User>> getCurrentUser();
}