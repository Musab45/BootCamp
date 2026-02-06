class ServerException implements Exception{
  final String message;
  final int? statusCode;

  ServerException({
    required this.message,
    this.statusCode,
  });

  @override
  String toString() => message;
}

class CacheException implements Exception{
  final String message;

  CacheException({
    required this.message,
  });

  @override
  String toString() => message;
}

class NetworkException implements Exception{
  final String message;

  NetworkException({
    required this.message,
  });

  @override
  String toString() => message;
}

class UnauthorizedException implements Exception{
  final String message;

  UnauthorizedException({
    this.message = 'Unauthorized. Please login again.',
  });

  @override
  String toString() => message;
}

class ValidationException implements Exception{
  final String message;
  final Map<String, List<String>>? errors;

  ValidationException({
    required this.message,
    this.errors,
  });

  @override
  String toString() => message;
}