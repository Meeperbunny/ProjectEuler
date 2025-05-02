cmake_minimum_required(VERSION 3.20)
project(prime_power_count LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS  OFF)

# Speed flags
if(NOT CMAKE_CXX_FLAGS MATCHES "-O")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -march=native")
endif()

# ─── Bring in libprimecount (v7.17) ──────────────────────────────────────────────
include(FetchContent)
FetchContent_Declare(
  primecount
  GIT_REPOSITORY https://github.com/kimwalisch/primecount.git
  GIT_TAG        v7.17
)
FetchContent_MakeAvailable(primecount)   # builds libprimecount + libprimesieve

# ─── Your program ───────────────────────────────────────────────────────────────
add_executable(euler268 scripts/268.cc)   # adjust name / path if desired
target_link_libraries(euler268 PRIVATE primecount::primecount)
