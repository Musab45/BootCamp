class ApiConstants {
  // base
  static const String baseUrl = 'http://127.0.0.1:8000/api/v1';

  // auth
  static const String login = '/auth/login';
  static const String register = '/auth/register';
  static const String token = '/auth/token';

  // user
  static const String profile = '/users/me';
  static const String updateProfile = '/users/me';
  static const String changePassword = '/users/me/change-password';

  // timeout
  static const Duration connectionTimeout = Duration(seconds: 30);
  static const Duration receiveTimeout = Duration(seconds: 30);
}