class element_has_attribute_with_value(object):

    def __init__(self, locator_or_element, attribute_name, attribute_value):
        self.locator_or_element = locator_or_element
        self.attribute_name = attribute_name
        self.attribute_value = attribute_value

    def __call__(self, driver):
        if type(self.locator_or_element) is tuple:
            element = driver.find_element(*self.locator_or_element)
        else:
            element = self.locator_or_element
        if self.attribute_value in element.get_attribute(self.attribute_name):
            return element
        else:
            return False


class element_has_correct_image_path(object):

    def __init__(self, locator, image_path):
        self.locator = locator
        self.image_path = image_path

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if self.image_path.split('/')[-1] in element.get_attribute("value").split('\\')[-1]:
            return element
        else:
            return False
