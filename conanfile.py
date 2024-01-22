#conan create .. --build=osi_vizualiser/0.1 --options=qt/5.15.12:shared=True


from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.scm import Git
from conan.tools.build import check_max_cppstd, check_min_cppstd


class OSIVizualiserRecipe(ConanFile):
    name = "osi_vizualiser"
    version = "0.1"

    # Optional metadata
    license = ""
    author = "Ahmed Attia"
    url = ""
    description = "<Description of hello package here>"
    topics = ("OSI")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": True, "fPIC": True}

    generators = "CMakeDeps"
    exports_sources = "CMakeLists.txt", "src/*", "include/*", "open-simulation-interface/*", "resources/*"
    
    def validate(self):
        check_min_cppstd(self, "11")
        check_max_cppstd(self, "20")

    #def source(self):
        #git = Git(self)
        #git.clone(url="https://github.com/conan-io/libhello.git", target=".")
        # Please, be aware that using the head of the branch instead of an immutable tag
        # or commit is not a good practice in general
        #git.checkout("require_fmt")

    def requirements(self):
        self.requires("protobuf/3.17.1")
        self.requires("qt/5.15.12")
        self.requires("cppzmq/4.10.0")
        self.requires("fmi_library/2.4.1")

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    # def package_info(self):
    #     self.cpp_info.libs = ["hello"]