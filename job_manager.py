import copy


def create_shallow_copy(job_template):
    return copy.copy(job_template)


def create_deep_copy(job_template):
    return copy.deepcopy(job_template)