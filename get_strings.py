class SemanticVersion():
    def __init__(self, major, minor, patch):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self):
        result = f"{str(self.major)}.{str(self.minor)}.{str(self.patch)}"
        return result


def main():
    py370 = SemanticVersion(major=3, minor=7, patch=0)
    print("3.7.0" == str(py370))


if __name__ == "__main__":
    main()
